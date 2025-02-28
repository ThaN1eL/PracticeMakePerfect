document.addEventListener('alpine:init', () => {
    Alpine.data('products', () => ({
        items: [
            { id: 1, name: 'Omnipotence Staff', img: 'product2.png', price: 1000, description: 'Staff imbued with limitless power.' },
            { id: 2, name: 'Megumin Hat', img: 'product3.png', price: 300, description: 'The explosion mage of Megumin.' },
            { id: 3, name: 'Omnipotence Grimoire', img: 'product1.png', price: 5555, description: 'Ancient grimoire containing limitless spells.' },
            { id: 4, name: 'Holy Wand Court Emblem', img: 'product5.png', price: 2250, description: 'Emblem blessed by the court mages.' }
        ]
    }));

    Alpine.store('cart', {
        items: [],
        total: 0,
        quantity: 0,
        add(newItem) {
            const cartItem = this.items.find((item) => item.id === newItem.id);
            if (!cartItem) {
                this.items.push({ ...newItem, quantity: 1, total: newItem.price });
                this.quantity++;
                this.total += newItem.price;
            } else {
                this.items = this.items.map((item) => {
                    if (item.id !== newItem.id) {
                        return item;
                    } else {
                        item.quantity++;
                        item.total = item.price * item.quantity;
                        this.quantity++;
                        this.total += item.price;
                        return item;
                    }
                });
            }
        },
        remove(id) {
            const cartItem = this.items.find((item) => item.id === id);
            if (cartItem.quantity > 1) {
                this.items = this.items.map((item) => {
                    if (item.id !== id) {
                        return item;
                    } else {
                        item.quantity--;
                        item.total = item.price * item.quantity;
                        this.quantity--;
                        this.total -= item.price;
                        return item;
                    }
                });
            } else if (cartItem.quantity === 1) {
                this.items = this.items.filter((item) => item.id !== id);
                this.quantity--;
                this.total -= cartItem.price;
            }
        },
    });

    Alpine.store('modal', {
        selectedItem: [],
        open(item) {
            this.selectedItem = item;
            document.querySelector('#item-detail-modal').style.display = 'flex';
        },
        close() {
            this.selectedItem = [];
            if (this.selectedItem.length === 0)
            document.querySelector('#item-detail-modal').style.display = 'none';
            document.querySelector('#modal-image').src = '';
        }
    });
});

const USD = (number) => {
    return new Intl.NumberFormat('usa-EN', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2,
    }).format(number);
};