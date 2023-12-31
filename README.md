> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、服务名、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# fc-embedding-api 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-embdding-api&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc-embedding-api" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-embedding-api&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc-embedding-api" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-embedding-api&type=packageDownload">
  </a>
</p>

<description>
部署 embedding服务到函数计算上

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/fc-embedding-api)

</codeUrl>
<preview>

</preview>

## 前期准备

使用该项目，您需要有开通以下服务：

<service>

| 服务         | 备注                                                                                                  |
| ------------ | ----------------------------------------------------------------------------------------------------- |
| 函数计算 FC  | 对 AIGC 进行 CPU 推理计算                                                                             |
| 文件存储 NAS | 存储 AIGC 的模型, 新用户请先领取免费试用资源包https://free.aliyun.com/?product=9657388&crowd=personal |

</service>

推荐您拥有以下的产品权限 / 策略：
<auth>
</auth>

<remark>

您还需要注意：  
1.项目依赖阿里云函数计算和阿里云文件存储 Nas，这两款产品都会产生资费，请关注您的资源包使用情况和费用情况 2.项目部署成功之后确保模型加载完毕（左上角选择框有模型显示）再开始推理 3.项目初始启动有大约 1 分钟的白屏时间，这是服务完全冷启动的状态，请耐心等待

</remark>

<disclaimers>

免责声明：

1. 该项目的构建镜像及应用模板完全开源，由社区开发者贡献，阿里云仅提供了算力支持；

</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=fc-chat) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=fc-chat) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init fc-chat -d fc-chat `
  - 进入项目，并进行项目部署：`cd fc-chat && s deploy - y`
   
</deploy>

## 应用详情

<appdetail id="flushContent">

## 前期准备

使用该项目，您需要有开通以下服务：

| 服务         | 备注 |
| ------------ | ---- |
| 函数计算 FC  |      |
| 文件存储 NAS |      |

推荐您拥有以下的产品权限 / 策略：

## 应用介绍文档

### 应用详情

本应用旨在帮助开发者实现将Sentence Transformers应用部署到阿里云函数计算，并且提供动态管理模型插件等能力

## 使用文档

### 本地部署方案

- 安装 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 开发者工具`npm install @serverless-devs/s -g`
  ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
- 初始化项目：`s init fc-embedding-api -d fc-embedding-api`
- 进入项目，并进行项目部署：`cd fc-embedding-api && s deploy - y`
  本地部署成功后使用部分参考应用中心部署方案配置管理后台系列操作

</appdetail>

## 使用文档

<usedetail id="flushContent">

### 常见问题


</usedetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |

</p>
</devgroup>
