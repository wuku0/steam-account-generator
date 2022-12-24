const puppeteer = require('puppeteer');

(async () => {
  // Set up Puppeteer
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Navigate to https://www.guerrillamail.com
  await page.goto('https://www.guerrillamail.com');

  // Click the "Copy" button to get the email
  const email = await page.evaluate(() => {
    document.querySelector('#copy-button').click();
    return document.querySelector('#email-widget').textContent;
  });

  // Navigate to https://www.dashlane.com/features/password-generator
  await page.goto('https://www.dashlane.com/features/password-generator');

  // Click the "Copy password" button to get the password
  await page.click('.button.button--primary');
  const password = await page.evaluate(() => {
    return document.querySelector('#password').textContent;
  });

  // Navigate to https://www.dashlane.com/features/password-generator again
  await page.goto('https://www.dashlane.com/features/password-generator');

  // Generate a username
  await page.type('#password', 'my_username');
  await page.click('#copy-button');
  const username = await page.evaluate(() => {
    return document.querySelector('#password').textContent;
  });

  // Navigate to the Steam sign-up page
  await page.goto('https://store.steampowered.com/join/');

  // Fill out the form on the sign-up page with the email, username, and password
  await page.type('#username', username);
  await page.type('#email', email);
  await page.type('#password', password);

  // Submit the form
  await page.click('button[type="submit"]');
  
 // Print the email, username, and password
 console.log(`Email: ${email}`);
 console.log(`Username: ${username}`);
 console.log(`Password: ${password}`);

  // Close the browser
  await browser.close();
})();