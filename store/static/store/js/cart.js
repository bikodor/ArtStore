const cartItemsSection = document.getElementById('cart-items');
let cart = JSON.parse(localStorage.getItem('cart')) || [];

// Функция группировки товаров по ID
function groupCartItems(cart) {
    const groupedCart = {};
    cart.forEach(item => {
        if (groupedCart[item.id]) {
            groupedCart[item.id].count++;
        } else {
            groupedCart[item.id] = { ...item, count: 1 };
        }
    });
    return Object.values(groupedCart); // Возвращаем массив объектов с группировкой и счетчиком
}

let groupedCart = groupCartItems(cart);

// Отображение товаров в корзине
function renderCartItems() {
    cartItemsSection.innerHTML = ''; // Очищаем контейнер перед рендером
    groupedCart.forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.classList.add('cart-item');
        cartItem.innerHTML = `
            <img src="${item.image}" alt="${item.name}">
            <h3>${item.name}</h3>
            <p>Price: $${item.price}</p>
            <p class="item-count">${item.count > 1 ? `x${item.count}` : ''}</p>
            <button class="remove-button" onclick="removeFromCart(${item.id})">X</button>
        `;
        cartItemsSection.appendChild(cartItem);
    });
}

// Функция удаления товара
function removeFromCart(productId) {
    const productIndex = cart.findIndex(p => p.id === productId);
    if (productIndex > -1) {
        if (groupedCart.find(item => item.id === productId).count > 1) {
            // Если товара несколько, уменьшаем количество
            cart.splice(productIndex, 1);
        } else {
            // Если товар один, удаляем его полностью
            cart = cart.filter(p => p.id !== productId);
        }
        groupedCart = groupCartItems(cart);
        localStorage.setItem('cart', JSON.stringify(cart));
        renderCartItems(); // Обновляем отображение корзины
    }
}

// Рендер товаров при загрузке страницы
renderCartItems();

// Очистка корзины после завершения
document.getElementById('checkout-button').addEventListener('click', () => {
    alert("Thank you for your purchase!");
    localStorage.removeItem('cart');
    groupedCart = [];
    renderCartItems();
});
