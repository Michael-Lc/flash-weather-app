const search = document.getElementById("search");
const form = document.getElementById("search-form");
const list = document.getElementById("auto-complete");

search.addEventListener("input", function (event) {
  const value = this.value;

  if (!value) return false;

  const query = `http://api.weatherapi.com/v1/search.json?key=d2282deb52c74c0691013155210302&q=${value}`;
  fetch(query)
    .then((response) => response.json())
    .then((cities) => {
      // create array of list items and append them to ul under search
      let items = ``,
        count = 0;
      for (const city of cities) {
        if (count > 3) break;
        items += `<li class="auto-complete-item">${city.name}</li>`;
        count += 1;
      }
      list.innerHTML = items;

      const listItems = document.getElementsByClassName("auto-complete-item");

      for (const item of listItems) {
        item.addEventListener("click", function (event) {
          const query = event.target.innerText;
          search.value = query;
          form.submit();
          // fetch("/", { method: "POST", body: query });
          search.value = "";
          list.innerHTML = "";
        });
      }
    })
    .catch((err) => console.log(err));
});
