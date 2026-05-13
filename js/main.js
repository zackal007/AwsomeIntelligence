// 主要的JavaScript功能
document.addEventListener('DOMContentLoaded', function() {
    // 平滑滚动到锚点
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // 添加简单的表单验证（如果需要）

    // "更多"按钮功能
    const mediaMoreBtn = document.getElementById('media-more-btn');
    const mediaMoreContent = document.getElementById('media-more-content');
    
    if (mediaMoreBtn && mediaMoreContent) {
        mediaMoreBtn.addEventListener('click', function() {
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', !isExpanded);
            mediaMoreContent.hidden = isExpanded;
            
            // 更新按钮文本
            if (isExpanded) {
                this.textContent = '更多';
            } else {
                this.textContent = '收起';
            }
        });
    }
    // 可以在这里添加更多交互功能

    console.log('网站已加载完成');
});