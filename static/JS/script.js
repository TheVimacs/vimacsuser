const menuIcon = document.querySelector(".menuIcon");
const navMenu = document.querySelector(".navMenu");
menuIcon.addEventListener("click", menuFunc);
function menuFunc() {
	if (menuIcon.classList.contains("active")) {
		navMenu.classList.remove("active");
		menuIcon.classList.remove("active");
		menuIcon.classList.add("close");
		navMenu.classList.add("close");
	} else {
		menuIcon.classList.remove("close");
		navMenu.classList.remove("close");
		menuIcon.classList.add("active");
		navMenu.classList.add("active");
	}
}
const navLink = document.querySelectorAll(".navItem");
navLink.forEach(n => n.addEventListener("click", menuFunc));
