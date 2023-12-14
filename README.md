# DoubanTop250-WebCrawler
![GitHub](https://img.shields.io/github/license/electronic-pig/DoubanTop250-WebCrawler)
![GitHub Repo stars](https://img.shields.io/github/stars/electronic-pig/DoubanTop250-WebCrawler)

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

```
pip install -r requirements.txt
python app.py
```

## Docker部署
```
docker pull electronicpig/douban-webapp:latest
docker run -d --name douban-container -p 5000:5000 electronicpig/douban-webapp:latest
```
## 运行效果
> 主页面

![image](https://github.com/electronic-pig/DoubanTop250-WebCrawler/assets/103497254/655a439e-1f02-4bef-a8a0-63cb550e26f3)

> 电影列表页面

![image](https://github.com/electronic-pig/DoubanTop250-WebCrawler/assets/103497254/fef08b8c-1d85-4f83-ae16-eac79272b5b4)

