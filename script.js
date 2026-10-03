// Меню. Чтобы добавить блюдо — допишите объект в массив.
// Фото кладите в images/menu/<img>.jpg — если файла нет, показывается орнамент.
const MENU = [
  { name: "Ташкентский плов",   price: 595, weight: "420 г", cat: "hot",   img: "tashkent-plov",  badge: "Хит" },
  { name: "Самаркандский плов", price: 560, weight: "420 г", cat: "hot",   img: "samarkand-plov" },
  { name: "Манты",              price: 615, weight: "400 г", cat: "hot",   img: "manty" },
  { name: "Хонум",              price: 560, weight: "400 г", cat: "hot",   img: "honum",
    desc: "Нежный говяжий фарш, обёрнутый слоями в домашнее тесто" },
  { name: "Шурпа из говядины",  price: 480, weight: "300 г", cat: "soup",  img: "shurpa" },
  { name: "Самса Пармуда",      price: 270, weight: "200 г", cat: "bake",  img: "samsa-parmuda" },
  { name: "Чебурек с говядиной", price: 270, weight: "120 г", cat: "bake", img: "cheburek",
    desc: "Хрустящее тесто с начинкой из сочного говяжьего фарша" },
  { name: "Ачик-чучук",         price: 395, weight: "220 г", cat: "salad", img: "achik-chuchuk" },
  { name: "Аджапсандал",        price: 595, weight: "300 г", cat: "salad", img: "ajapsandal" },
];

const grid = document.getElementById("menu-grid");
const fmt = (n) => n.toLocaleString("ru-RU") + " ₽";

grid.innerHTML = MENU.map((d) => `
  <article class="dish reveal" data-cat="${d.cat}">
    <div class="dish__img">
      ${d.badge ? `<span class="dish__badge">${d.badge}</span>` : ""}
      <img src="images/menu/${d.img}.jpg" alt="${d.name}" loading="lazy" onerror="this.remove()">
    </div>
    <div class="dish__body">
      <h3>${d.name}</h3>
      ${d.desc ? `<p>${d.desc}</p>` : ""}
      <div class="dish__foot">
        <span class="dish__price">${fmt(d.price)}</span>
        <span class="dish__weight">${d.weight}</span>
      </div>
    </div>
  </article>`).join("");

// Фильтр по категориям
document.querySelectorAll(".tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((t) => {
      t.classList.toggle("is-active", t === tab);
      t.setAttribute("aria-selected", t === tab);
    });
    const f = tab.dataset.filter;
    grid.querySelectorAll(".dish").forEach((el) => {
      el.hidden = f !== "all" && el.dataset.cat !== f;
    });
  });
});

// Шапка: фон при прокрутке и мобильное меню
const nav = document.querySelector(".nav");
const burger = document.querySelector(".burger");
const onScroll = () => nav.classList.toggle("is-solid", window.scrollY > 40);
onScroll();
window.addEventListener("scroll", onScroll, { passive: true });

burger.addEventListener("click", () => {
  const open = nav.classList.toggle("is-open");
  burger.setAttribute("aria-expanded", open);
});
document.querySelectorAll(".nav__links a").forEach((a) =>
  a.addEventListener("click", () => {
    nav.classList.remove("is-open");
    burger.setAttribute("aria-expanded", "false");
  })
);

// Плавное появление блоков
document.querySelectorAll(".section__head, .about__text, .features li, .g, .reviews > *, .contacts > *")
  .forEach((el) => el.classList.add("reveal"));
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
  });
}, { threshold: 0.12 });
document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

document.getElementById("year").textContent = new Date().getFullYear();
