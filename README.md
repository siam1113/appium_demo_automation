# appium_demo_automation
Automating different application for demo purpose

### Get current activity of the running app
```bash
 dumpsys window windows | grep -E 'mCurrentFocus'
```

### How to start Appium Inspector and Start Inspecting
1. Start your virtual device
2. Run `appium` in command line
3. Start appium inspector session with `platformName` & `automationName`
