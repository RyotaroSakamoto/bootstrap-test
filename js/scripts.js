// 商品カードにホバーエフェクトを追加
document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseover', function() {
            card.style.transform = 'scale(1.05)';
            card.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
        });

        card.addEventListener('mouseout', function() {
            card.style.transform = 'scale(1)';
            card.style.boxShadow = 'none';
        });
    });
});
