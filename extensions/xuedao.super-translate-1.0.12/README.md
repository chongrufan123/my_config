<!--
 * @Descripttion: 
 * @Author: zhujiang
 * @Date: 2019-07-13 23:36:31
 * @LastEditors: zhujiang
 * @LastEditTime: 2020-04-23 16:40:04
 * @FilePath: \A-super-translate\README.md
 -->

# VSCode 注释翻译 [![](https://badgen.net/vs-marketplace/v/xuedao.super-translate)](https://marketplace.visualstudio.com/items?itemName=xuedao.super-translate) [![](https://badgen.net/vs-marketplace/i/xuedao.super-translate)](https://marketplace.visualstudio.com/items?itemName=xuedao.super-translate) [![](https://badgen.net/vs-marketplace/d/xuedao.super-translate)](https://marketplace.visualstudio.com/items?itemName=xuedao.super-translate) ![](https://img.shields.io/badge/license-MIT-F44336.svg)

欢迎来到懒人世界

[如果觉得好用，不要吝啬star(*^▽^*)](https://gitee.com/qq34347476/snippets)

今后更新更多懒人插件，欢迎提bugs,交流,关注,star：
[github](https://github.com/qq34347476)
[gitee](https://gitee.com/qq34347476)

## 简介

许多优秀的项目，都有丰富的注释，使用者可以快速理解代码意图。但是如果使用者并不熟习注释的语言，会带来理解困难。本插件使用 Google Translate API 翻译 VSCode 的编程语言的注释。

## 功能

> 使用方法：选中行，Alt+Shift+p 输入 翻译

+ 键入 Alt+`再按下 Alt+1 为翻译直接替换选中区域

+ 键入 Alt+` 再按下 Alt+2 为切换翻译语言

1. 识别代码中注释部分，不干扰阅读。支持不同语言，单行、多行注释
![Introduction](https://github.com/intellism/vscode-comment-translate/raw/master/./doc/image/cn/Introduction.gif)

2. 支持用户字符串与变量翻译,支持驼峰拆分
![Introduction](https://github.com/intellism/vscode-comment-translate/raw/master/./doc/image/cn/variable.gif)

3. 选择区域翻译 - 划词翻译
![Introduction](https://github.com/intellism/vscode-comment-translate/raw/master/./doc/image/cn/selection.gif)

4. 翻译并替换选择内容
![Introduction](https://github.com/intellism/vscode-comment-translate/raw/master/./doc/image/translate-selections.gif)

5. 选中最后一次翻译区域命令
![Introduction](https://github.com/intellism/vscode-comment-translate/raw/master/./doc/image/cn/select.gif)

## 配置项

#### 多国语言支持

状态栏快速配置目标语言
![Multi-language](https://github.com/intellism/vscode-comment-translate/raw/master/./doc/image/cn/status-bar.gif)

| Display Language    | Locale  |
| ------------------- | ------- |
| English (US)        | `en`    |
| Simplified Chinese  | `zh-CN` |
| Traditional Chinese | `zh-TW` |
| French              | `fr`    |
| German              | `de`    |
| Italian             | `it`    |
| Spanish             | `es`    |
| Japanese            | `ja`    |
| Korean              | `ko`    |
| Russian             | `ru`    |
| Bulgarian           | `bg`    |
| Hungarian           | `hu`    |
| Portuguese (Brazil) | `pt-br` |
| Turkish             | `tr`    |

#### 合并多行注释 （源语言只支持英语）

![Multi-line-merge](https://github.com/intellism/vscode-comment-translate/raw/master/./doc/image/multi-line-merge.gif)
