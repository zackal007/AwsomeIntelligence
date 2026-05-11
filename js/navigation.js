// 移动端导航菜单功能
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const navLinks = document.querySelector('.nav-links');
    
    if (mobileMenuButton && navLinks) {
        // 初始化aria-expanded
        mobileMenuButton.setAttribute('aria-expanded', 'false');
        
        mobileMenuButton.addEventListener('click', function() {
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            navLinks.classList.toggle('active');
            
            // 更新aria-expanded属性
            this.setAttribute('aria-expanded', !isExpanded);
            
            // 更新按钮图标（可选）
            const icon = this.textContent;
            this.textContent = icon === '☰' ? '✕' : '☰';
        });
        
        // 点击导航链接后关闭菜单
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                navLinks.classList.remove('active');
                mobileMenuButton.setAttribute('aria-expanded', 'false');
                mobileMenuButton.textContent = '☰';
            });
        });
        
        // 点击页面其他地方关闭菜单
        document.addEventListener('click', function(event) {
            if (!navLinks.contains(event.target) && 
                !mobileMenuButton.contains(event.target) && 
                navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                mobileMenuButton.setAttribute('aria-expanded', 'false');
                mobileMenuButton.textContent = '☰';
            }
        });
        
        // 键盘导航支持
        mobileMenuButton.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });
    }
});