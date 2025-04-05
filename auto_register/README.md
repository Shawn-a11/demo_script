# 自动注册脚本

这是一个自动化注册脚本，可以：
1. 自动登录 Outlook 邮箱
2. 打开指定网页并完成注册
3. 自动获取验证码并填写

## 功能特点

- 自动登录 Outlook
- 自动获取验证码
- 自动填写注册表单
- 支持自定义注册页面
- 包含错误处理机制

## 安装要求

1. Python 3.7 或更高版本
2. Chrome 浏览器
3. 安装依赖包：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. 编辑 `.env` 文件，填入必要信息：
   ```
   OUTLOOK_EMAIL=your_email@outlook.com
   OUTLOOK_PASSWORD=your_password
   IMAP_SERVER=outlook.office365.com
   REGISTRATION_URL=your_registration_url
   ```

2. 运行脚本：
   ```bash
   python auto_register.py
   ```

## 注意事项

- 请确保您的 Outlook 账号已启用 IMAP 访问
- 脚本中的 CSS 选择器需要根据实际的注册页面进行调整
- 验证码获取逻辑可能需要根据实际的邮件格式进行调整
- 如果遇到验证码识别问题，可能需要手动处理

## 安全提示

- 请妥善保管您的账号密码
- 不要将包含真实密码的 `.env` 文件分享给他人
- 建议定期更改密码

## 自定义配置

如果需要修改注册页面的元素选择器，请编辑 `auto_register.py` 文件中的 `register_account` 函数，根据实际的页面元素修改相应的 CSS 选择器。 