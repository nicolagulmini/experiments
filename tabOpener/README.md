# Open Tabs Chrome Extension

This is a simple Chrome extension that automatically opens specified URLs when you click on the extension icon. It's a great tool for quickly accessing frequently used websites.

## Features
- Opens multiple tabs with user-specified URLs.
- No need for a confirmation button—just click the extension icon, and your tabs will open!

## Installation Instructions

To install this unpacked Chrome extension, follow these steps:

### Step 1: Download or Clone the Repository

You can either clone this repository using Git:

```bash
git clone https://github.com/your-username/open-tabs-extension.git
```

Or download the zip file and extract it to a folder on your computer.

### Step 2: Open Chrome Extensions Page

1. Open Google Chrome.
2. In the address bar, type `chrome://extensions/` and press **Enter**.
3. Enable **Developer mode** by toggling the switch in the upper-right corner of the page.

### Step 3: Load the Unpacked Extension

1. Click the **Load unpacked** button at the top left of the page.
2. In the pop-up window, navigate to the folder where you saved/cloned the repository, and select the folder that contains the `manifest.json` file.
3. The extension will now be installed, and you will see the icon appear in the Chrome toolbar.

### Step 4: Use the Extension

Click on the extension icon in the toolbar, and the specified URLs will automatically open in new tabs.

## Customizing URLs

If you'd like to change the URLs that the extension opens, you can:

1. Open the `background.js` file located in the extension folder.
2. Replace the URLs in the array with your own:

```javascript
const urls = [
  "https://www.example.com",
  "https://www.google.com",
  "https://www.openai.com"
];
```

3. After saving your changes, go back to `chrome://extensions/` and click the **Reload** button next to your extension to apply the changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.