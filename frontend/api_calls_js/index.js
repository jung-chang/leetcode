class PokemonTable {
    constructor(maxRows) {
        this.pokemonList = [];
        this.maxRows = maxRows;

        this.nameSortAsc = false;
        this.heightSortAsc = false;
        this.weightSortAsc = false;

        this.table = document.querySelector("table.pokemon");
        this.table.querySelector("th.name").addEventListener("click", () => this.sortTable("name"));
        this.table.querySelector("th.height").addEventListener("click", () => this.sortTable("height"));
        this.table.querySelector("th.weight").addEventListener("click", () => this.sortTable("weight"));        
    }

    sortTable(dimension) {
        if (!this.pokemonList.length) {
            return;
        }
        console.log({dimension})
        if (dimension === "name") {
            this.pokemonList.sort((a, b) => {
                if (this.nameSortAsc) { return a.name > b.name }
                else { return a.name < b.name }
            });
            this.nameSortAsc = !this.nameSortAsc;
        } else if (dimension === "height") {
            this.pokemonList.sort((a, b) => {
                if (this.heightSortAsc) { return a.height > b.height }
                else { return a.height < b.height }
            });
            this.heightSortAsc = !this.heightSortAsc;
        } else if (dimension === "weight") {
            this.pokemonList.sort((a, b) => {
                if (this.weightSortAsc) { return a.weight > b.weight }
                else { return a.weight < b.weight }
            });
            this.weightSortAsc = !this.weightSortAsc;
        }
        this.populateTableWithPokemon(this.pokemonList);
    }
    
    populateTableWithPokemon(pokemonList) {
        const tbody = this.table.querySelector("tbody");
        tbody.innerHTML = "";
        for (const pokemon of pokemonList) {
            const pokemonRow = pokemon.generateTableRow();
            tbody.appendChild(pokemonRow);
        }
    };
    
    async generateTable() {
        const pokemonApiClient = new PokemonApiClient();
        const pokemonList = await pokemonApiClient.getPokemonList(10);
        if (!!pokemonList) {
            this.pokemonList = pokemonList;
        }
        this.populateTableWithPokemon(pokemonList);
    }
}

class Pokemon {
    constructor(name, height, weight, types) {
        this.name = name;
        this.height = height;
        this.weight = weight;
        this.types = types; 
    }

    generateTableRow() {
        const tr = document.createElement("tr");

        let td = document.createElement("td");
        td.innerHTML = this.name;
        tr.appendChild(td);

        td = document.createElement("td");
        td.innerHTML = this.height;
        tr.appendChild(td);

        td = document.createElement("td");
        td.innerHTML = this.weight;
        tr.appendChild(td);

        td = document.createElement("td");
        td.innerHTML = this.types.join(",");
        tr.appendChild(td);
        return tr;
    }
}

class PokemonApiClient {

    constructor() {
        // Name to Pokemon
        this.pokemonListCache = {};
    }

    updateCache(pokemonList) {

    }

    parseJsonToPokemon(name, jsonDetails) {
        const types = [];
        for (const type of jsonDetails["types"]) {
            types.push(type["type"]["name"]);
        }
        return new Pokemon(name, jsonDetails["height"] || 0, jsonDetails["weight"] || 0, types);
    } 

    async getPokemonList(limit=100) {
        return await fetch(`https://pokeapi.co/api/v2/pokemon?limit=${limit}`, {
            method: "GET",
        }).then((response) => response.json()).then(async (jsonData) => {
            const pokemonList = [];
            const results = jsonData["results"];
            for (const result of results) {
                if (!!this.pokemonListCache[result["name"]]) {
                    console.log(["cache hit", result["name"]]);
                    pokemonList.push(this.pokemonListCache[result["name"]]);
                } else {
                    const details = await this.getPokemon(result["name"]);
                    pokemonList.push(this.parseJsonToPokemon(result["name"], details));
                }
            }
            this.updateCache(pokemonList);
            return pokemonList;
        })
        .catch((reason) => console.error({reason}));
    }

    async getPokemon(name) {
        return await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`, {
            method: "GET",
        }).then((response) => response.json()).catch((reason) => console.error({reason}));
    }

    searchPokemon(searchString) {
        return;
    }
}

const table = new PokemonTable(5);
table.generateTable();