# Android 测试构建

本分支用于 Android 真机测试，不代表 Google Play 或其他商店正式发行版本。

## 构建基线

- Ren'Py：8.5.3
- RAPT：与 Ren'Py 8.5.3 配套的官方版本
- Android API：36
- Java：JDK 21
- 包名：`com.caomloas.alpha01awakening`
- 屏幕方向：横屏，允许设备在两个横屏方向间旋转
- 商店内购：未启用

## 本地构建

将 RAPT 安装到 Ren'Py SDK 后，为 RAPT 指定本机 Android SDK，并确保 `JAVA_HOME` 指向 JDK 21。Ren'Py 8.5.3 会在构建前校验 Java 主版本，JDK 17 无法通过这一检查。然后运行：

```text
renpy <Ren'Py SDK 内的 launcher 目录> android_build <项目目录> --destination <输出目录>
```

需要直接部署到已连接设备时，可追加 `--install --launch`。

## 安全说明

`android.keystore`、`bundle.keystore`、JDK、Android SDK、本机路径和编译缓存均不提交。当前 APK 使用测试签名；正式发布前必须建立独立、妥善备份的发布密钥，并提高 Android 版本号。

## v0.2.3 测试包

- versionName 0.2.3；配置 numeric_version 最低值为 5，RAPT 实际取与构建时间戳的较大值，本包 versionCode 为 1789224453。保留原包名及本机原测试签名，不创建新密钥。
- 含晴空主菜单、小龙入场、水纹、统一的 X／抖音／制作组图标。
- 约稿应用图标通过 `design/prepare-commissioned-icon.py <用户原图路径>` 机械缩放生成，中央留边适配启动器遮罩；使用范围见 `COMMISSIONED_ICON_NOTICE.md`。
- 仅构建、检查 APK 结构与签名，不执行 ADB 安装。用户自行实机验收。覆盖更新仍以设备上旧包具有相同签名为前提；不要为解决安装报错先卸载旧版，以免丢失存档。
- 验证：lint、compile 通过；APK v1/v2 签名验证通过，与上一份本地 v0.2.2 APK 公共签名证书一致；最低 API 21、目标 API 36、sensorLandscape；包含 arm64-v8a、armeabi-v7a、x86_64。签名工具提示若干 META-INF 元数据不受 v1 单项签名保护，但整包 v2 校验通过，未改写签名产物。
