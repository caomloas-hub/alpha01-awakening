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

将 RAPT 安装到 Ren'Py SDK 后，为 RAPT 指定本机 Android SDK，并确保 `JAVA_HOME` 指向 JDK 21。然后运行：

```text
renpy launcher android_build <项目目录> --destination <输出目录>
```

需要直接部署到已连接设备时，可追加 `--install --launch`。

## 安全说明

`android.keystore`、`bundle.keystore`、JDK、Android SDK、本机路径和编译缓存均不提交。当前 APK 使用测试签名；正式发布前必须建立独立、妥善备份的发布密钥，并提高 Android 版本号。
