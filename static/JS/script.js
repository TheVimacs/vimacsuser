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


document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('dark-mode-toggle');
    const lightMode = document.getElementById('light-mode');
    const darkMode = document.getElementById('dark-mode');
    const isDarkMode = localStorage.getItem('theme') === 'dark';
    const applyTheme = (theme) => {
        document.documentElement.setAttribute('data-theme', theme);
        if (theme === 'dark') {
            lightMode.classList.remove('hidden');
            darkMode.classList.add('hidden');
        } else {
            lightMode.classList.add('hidden');
            darkMode.classList.remove('hidden');
        }
    };
    toggle.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        applyTheme(newTheme);
        localStorage.setItem('theme', newTheme);
    });
    applyTheme(isDarkMode ? 'dark' : 'light');
});

