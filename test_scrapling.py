#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Scrapling 工具测试脚本
由于网络问题无法直接安装，这里展示如何使用 Scrapling 的基本用法
"""

# 如果 Scrapling 安装成功，可以取消下面的注释
# from scrapling import StealthyFetcher, Selector

def test_basic_scraping():
    """
    展示 Scrapling 的基本用法
    """
    print("=== Scrapling 功能演示 ===")
    print()
    
    # 1. 基本的静态页面抓取
    print("1. 静态页面抓取示例:")
    print("   fetcher = StealthyFetcher()")
    print("   response = fetcher.fetch('https://example.com')")
    print("   selector = Selector(response.text)")
    print("   title = selector.css('title::text').get()")
    print()
    
    # 2. 自适应选择器（处理页面结构变化）
    print("2. 自适应选择器示例:")
    print("   # 即使页面结构变化，也能找到目标元素")
    print("   price = selector.adaptive_css('.price, .cost, .amount')")
    print()
    
    # 3. 处理反爬虫
    print("3. 绕过反爬虫示例:")
    print("   # StealthyFetcher 自动处理 Cloudflare 等反爬虫")
    print("   fetcher = StealthyFetcher(stealthy=True)")
    print("   response = fetcher.fetch('https://protected-site.com')")
    print()
    
    # 4. 蜘蛛框架
    print("4. 蜘蛛爬取示例:")
    print("   from scrapling import Spider")
    print("   ")
    print("   class MySpider(Spider):")
    print("       start_urls = ['https://example.com']")
    print("       ")
    print("       async def parse(self, response):")
    print("           selector = Selector(response.text)")
    print("           for item in selector.css('.item'):")
    print("               yield {")
    print("                   'title': item.css('.title::text').get(),")
    print("                   'price': item.css('.price::text').get()")
    print("               }")
    print()
    
    print("注意: 由于网络连接问题，Scrapling 未能成功安装。")
    print("建议在网络环境更好的情况下重新尝试安装:")
    print("pip install scrapling")
    print()
    print("或者从 GitHub 克隆源码安装:")
    print("git clone https://github.com/D4Vinci/Scrapling.git")
    print("cd Scrapling")
    print("pip install -e .")

if __name__ == "__main__":
    test_basic_scraping()