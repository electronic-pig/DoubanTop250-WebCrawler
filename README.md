# DoubanTop250-WebCrawler
![GitHub](https://img.shields.io/github/license/electronic-pig/DoubanTop250-WebCrawler)
[![build status](https://github.com/electronic-pig/DoubanTop250-WebCrawler/actions/workflows/main.yml/badge.svg)](https://github.com/electronic-pig/DoubanTop250-WebCrawler/actions)
![python version](https://img.shields.io/badge/python-3.7+-orange.svg)
![GitHub Repo stars](https://img.shields.io/github/stars/electronic-pig/DoubanTop250-WebCrawler)

## ✨ 项目简介
豆瓣Top250电影列表网络爬虫+数据可视化Web应用

## 📁 项目结构
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

## 🚀 项目运行
```
pip install -r requirements.txt
python app.py
```

## 🐳 Docker部署
```
docker pull electronicpig/douban-webapp:latest
docker run -d --name douban-webapp -p 8000:8000 electronicpig/douban-webapp:latest
```

## 📸 运行截图
> 主页面

![image](https://github.com/electronic-pig/DoubanTop250-WebCrawler/assets/103497254/655a439e-1f02-4bef-a8a0-63cb550e26f3)

> 电影列表页面

![image](https://github.com/electronic-pig/DoubanTop250-WebCrawler/assets/103497254/fef08b8c-1d85-4f83-ae16-eac79272b5b4)

## ✍ 写在最后
项目制作不易，如果它对你有帮助的话，请务必给作者点一个免费的⭐，万分感谢!🙏🙏🙏
