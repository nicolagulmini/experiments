chrome.action.onClicked.addListener(() => {
  const urls = [
    "https://www.facebook.com/",
    "https://mail.google.com/",
    "https://www.youtube.com/",
    "https://github.com/",
  ];

  urls.forEach(url => {
    chrome.tabs.create({ url: url });
  });
});
