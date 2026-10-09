# 接入 www.zhou-wei.com

## 当前状态

2026-10-09 查询结果：`www.zhou-wei.com` 为 NXDOMAIN，根域 `zhou-wei.com` 没有 A 记录；SOA 指向阿里云域名 DNS。域名注册与 DNS 管理账号不通过这些结果推断。

本站先发布到 https://xiaomao361.github.io/zhou-wei.com/ 。先不设置 CNAME，避免默认地址跳转到尚未解析的域名。

## 待执行

1. 在 GitHub Pages 的自定义域名验证流程中生成域名验证 TXT 值，并在域名 DNS 管理处填写确切的验证记录。
2. 添加 DNS 记录：类型 `CNAME`，主机记录 `www`，值 `xiaomao361.github.io`（不含 HTTPS、仓库名或路径）。
3. 验证 DNS 返回上述值后，在**本项目仓库**设置 Pages 自定义域名 `www.zhou-wei.com`。不要配置账号根站的域名，以免改变收下等项目站点的地址继承关系。
4. 等待 GitHub 签发证书，开启强制 HTTPS，并验证真实域名页面与资源。
5. 再更新站点分享 metadata、404 返回链接与 GitHub 个人主页入口。

根域是否跳转到 www 可在接入时确定；只有 www 接入不是根域接入成功。

官方说明：

- [域名验证](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)
- [管理自定义域名](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

DNS 凭据不写入仓库或聊天。
