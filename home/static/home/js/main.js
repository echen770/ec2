const collapsibles = document.querySelectorAll(".collapsible");
collapsibles.forEach((item) =>
  item.addEventListener("click", function () {
    this.classList.toggle("nav__list_expanded");
  })
);

function setValue() {
  document.getElementById("checked").checked=true;
}

window.onload = setValue;