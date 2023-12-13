# DoubanTop250-WebCrawler
![GitHub](https://img.shields.io/github/license/electronic-pig/DoubanTop250-WebCrawler)

豆瓣Top250电影列表网络爬虫+数据可视化Web应用

## 主要文件结构
```
│  app.py                  //flask应用入口
│  dockerfile              //docker部署文件
│  movieTop250.db          //sqlite数据库文件
│  requirements.txt        //项目依赖文件
│  WebCrawler.py           //网页爬虫文件
│  wordCloud.py            //词云生成文件
├─static                   
│  └─assets                //静态资源文件
├─templates                //项目页面文件
│      index.html
│      movie.html
│      score.html
│      team.html
│      word.html
├─github
│  └─workflows
|        main.yml          //github Actions 自动化部署配置文件
        
```
## 项目运行


### 安装项目依赖
```
pip install -r requirements.txt
```
### 启动web项目
```
python app.py
```
## 运行效果
> 主页面

![网页捕获_30-9-2023_14721_20 18 120 71](https://github.com/electronic-pig/DoubanTop250-WebCrawler/assets/103497254/11a73b18-299b-4fb4-8b6b-e253b23f4278)
> 电影列表页面

![屏幕截图 2023-09-30 152110](https://github.com/electronic-pig/DoubanTop250-WebCrawler/assets/103497254/d3415200-74a5-4454-9f11-bbb8a5596f79)
