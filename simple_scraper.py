#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单网页爬虫示例
使用 requests + BeautifulSoup 实现基本的网页抓取功能
"""

import requests
from bs4 import BeautifulSoup
import time

def scrape_website(url):
    """
    简单的网页抓取函数
    """
    try:
        # 设置请求头模拟浏览器
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        print(f"正在抓取: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取基本信息
        title = soup.find('title')
        if title:
            print(f"页面标题: {title.get_text().strip()}")
        
        # 提取所有链接
        links = soup.find_all('a', href=True)
        print(f"找到 {len(links)} 个链接")
        
        # 提取段落文本
        paragraphs = soup.find_all('p')
        if paragraphs:
            print(f"前3个段落预览:")
            for i, p in enumerate(paragraphs[:3]):
                text = p.get_text().strip()
                if text:
                    print(f"  {i+1}. {text[:100]}...")
        
        return soup
        
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return None
    except Exception as e:
        print(f"解析错误: {e}")
        return None

def main():
    """
    主函数 - 测试爬虫
    """
    print("=== 简单网页爬虫测试 ===\n")
    
    # 测试几个网站
    test_urls = [
        'https://httpbin.org/html',
        'https://example.com'
    ]
    
    for url in test_urls:
        result = scrape_website(url)
        if result:
            print(f"[+] 成功抓取 {url}\n")
        else:
            print(f"[-] 抓取失败 {url}\n")
        
        # 避免过于频繁的请求
        time.sleep(1)

if __name__ == "__main__":
    main()