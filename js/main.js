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

    // 社交媒体"更多"按钮功能（预留扩展）
    const mediaMoreBtn = document.getElementById('media-more-btn');
    if (mediaMoreBtn) {
        mediaMoreBtn.addEventListener('click', function() {
            // 这里可以添加未来扩展功能
            console.log('更多按钮被点击');
        });
    }
    // 可以在这里添加更多交互功能

    console.log('网站已加载完成');
});