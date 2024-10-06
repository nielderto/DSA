class Array {
    constructor () {
        this.length = 0;
        this.data = {};
    }

    push(item) {
        this.data[this.length] = item;
        this.length += 1;
    }

    get(index) {
        return this.data[index];
    }

    pop() {
        let lastItem = this.data[this.length - 1];
        delete this.data[this.length - 1];
        this.length -= 1
        return lastItem;
    }

    delete(index) {
        let deletedItem = this.data[index];
        for (let i = index; i < this.length - 1; i++) {
            this.data[i] = this.data[i+1];
        }
        delete this.data[this.length-1];
        this.length -= 1;
        return deletedItem;
    }
}


const arr = new Array();
arr.push(10);
arr.push(20);
arr.push(30);
arr.push(40);
console.log(arr.delete(1)); 
console.log(arr);