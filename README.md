# Zhou Wei · 做点东西

个人作品主页，展示日常小工具、AI 工具和掌机游戏。

网站：https://xiaomao361.github.io/zhou-wei.com/

## 本地维护

无需安装运行依赖。使用 Node.js 与 Python 3：

```sh
npm run build
npm run preview
```

`index.html` 维护内容，`styles.css` 维护样式，`assets/` 保存网站实际使用的素材。所有路径兼容 GitHub Pages 项目子目录。

GitHub Pages 从 `main` 分支根目录发布。每次推送后由 GitHub 自动部署。`.nojekyll` 保持原生静态文件发布。

## 素材与验证

- [素材来源与使用边界](docs/ASSETS.md)
- [设计与验收记录](docs/DESIGN.md)
- [自定义域名接入](docs/DOMAIN.md)

`npm run check` 检查本地素材、锚点、图片尺寸字段、标题结构、HTTPS 链接与 SVG 格式；构建产物输出到 `dist/`。这些检查不证明实际浏览器中的布局、触控或键盘体验已验收。
