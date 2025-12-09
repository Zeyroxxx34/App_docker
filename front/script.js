//Récupération des items depuis l'API
fetch('http://api:5000/items')
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById('items');
        data.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item.name;
            list.appendChild(li);
        });
        print(data);
        console.log(data);
    });