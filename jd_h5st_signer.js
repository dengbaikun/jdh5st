const fs = require('fs');
const path = require('path');
const XMLHttpRequest = require('xhr2');

const DEFAULT_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36';

function createBrowserShim() {
  const store = new Map();

  function Element() {}
  Element.prototype = {
    scrollIntoViewIfNeeded() {},
  };

  function Document() {}
  Document.prototype = {
    querySelector() {
      return null;
    },
  };

  const canvasContext = {
    fillRect() {},
    arc() {},
    stroke() {},
    fillText() {},
    lineWidth: 0,
    lineCap: '',
    fillStyle: '',
    strokeStyle: '',
    font: '',
    textBaseline: '',
    shadowOffsetX: 0,
    shadowOffsetY: 0,
    shadowColor: '',
  };

  const document = new Document();
  document.cookie = '';
  document.createElement = () => ({
    style: {},
    type: '',
    readyState: null,
    parentNode: { removeChild() {} },
    setAttribute() {},
    getContext() {
      return canvasContext;
    },
    toDataURL() {
      return 'data:image/png;base64,';
    },
  });
  document.getElementsByTagName = () => [{
    appendChild(element) {
      if (element.onload) setTimeout(element.onload, 0);
    },
  }];
  document.head = {
    appendChild(element) {
      if (element.onload) setTimeout(element.onload, 0);
    },
  };
  document.documentElement = { appendChild() {} };
  document.querySelector = Document.prototype.querySelector;

  global.window = global;
  global.self = global;
  global.Element = Element;
  global.Document = Document;
  global.document = document;
  global.navigator = {
    userAgent: DEFAULT_UA,
    language: 'zh-CN',
    languages: ['zh-CN', 'zh'],
    platform: 'Win32',
  };
  global.location = {
    href: 'https://item.jd.com/100071422470.html',
    protocol: 'https:',
    host: 'item.jd.com',
  };
  global.localStorage = {
    getItem: (key) => store.get(key) || null,
    setItem: (key, value) => store.set(key, String(value)),
    removeItem: (key) => store.delete(key),
  };
  global.XMLHttpRequest = XMLHttpRequest;
  global.getComputedStyle = () => ({});
}

async function signInChrome(input, jsPath) {
  let puppeteer;
  try {
    puppeteer = require('puppeteer-core');
  } catch (error) {
    return null;
  }

  const executablePath = input.chromePath || process.env.CHROME_PATH || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  if (!fs.existsSync(executablePath)) {
    return null;
  }

  const browser = await puppeteer.launch({
    executablePath,
    headless: 'new',
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-blink-features=AutomationControlled',
    ],
  });

  try {
    const page = await browser.newPage();
    await page.setUserAgent(input.userAgent || DEFAULT_UA);
    for (let attempt = 0; attempt < 3; attempt += 1) {
      try {
        await page.goto(input.pageUrl || 'https://item.jd.com/100071422470.html', {
          waitUntil: 'networkidle2',
          timeout: 30000,
        });
        await page.waitForTimeout(1000);
        await page.addScriptTag({ path: jsPath });
        break;
      } catch (error) {
        if (attempt === 2) throw error;
        await page.waitForTimeout(1000);
      }
    }
    await page.waitForFunction(() => typeof window.ParamsSignMain === 'function', { timeout: 10000 });
    const signed = await page.evaluate(async ({ appId, params, waitMs }) => {
      const signer = new window.ParamsSignMain({ appId, debug: false });
      await new Promise((resolve) => setTimeout(resolve, waitMs));
      return signer.sign(params);
    }, {
      appId: input.appId || 'fb5df',
      params: input.params,
      waitMs: input.waitMs || 1800,
    });
    signed.__cookies = await page.cookies();
    return signed;
  } finally {
    await browser.close();
  }
}

async function main() {
  createBrowserShim();

  const stdin = await new Promise((resolve, reject) => {
    let data = '';
    process.stdin.setEncoding('utf8');
    process.stdin.on('data', (chunk) => {
      data += chunk;
    });
    process.stdin.on('end', () => resolve(data));
    process.stdin.on('error', reject);
  });
  const input = JSON.parse(stdin);
  const jsPath = path.join(__dirname, 'js_security_v3_main_0.1.8.js');
  const browserSigned = input.preferMock ? null : await signInChrome(input, jsPath);
  if (browserSigned) {
    process.stdout.write(JSON.stringify(browserSigned));
    return;
  }

  const code = fs.readFileSync(jsPath, 'utf8');
  eval(code);

  if (typeof ParamsSignMain !== 'function') {
    throw new Error('ParamsSignMain not loaded');
  }

  const signer = new ParamsSignMain({
    appId: input.appId || 'fb5df',
    debug: Boolean(input.debug),
  });

  await new Promise((resolve) => setTimeout(resolve, input.waitMs || 1800));
  const signed = await signer.sign(input.params);
  process.stdout.write(JSON.stringify(signed));
}

main().catch((error) => {
  process.stderr.write(error && error.stack ? error.stack : String(error));
  process.exit(1);
});
