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

document.addEventListener('DOMContentLoaded', function() {
    const toc = document.getElementById('toc');
    const subHeads1 = document.querySelectorAll('.subHead-1');
    
    subHeads1.forEach(function(subHead1) {
        const li1 = document.createElement('li');
        li1.classList.add('toc-itemo', 'tocSick');
        const tocToggler = document.createElement('span');
        tocToggler.textContent = '[x]';
        tocToggler.classList.add('tocToggler');
        li1.appendChild(tocToggler);
        const a1 = document.createElement('a');
        a1.href = '#' + subHead1.id;
        a1.textContent = subHead1.textContent;
        li1.appendChild(a1);
        const subHeads2listo = document.createElement('ul');
        subHeads2listo.classList.add('toc-listo');
        let nextElement = subHead1.nextElementSibling;
        
        while (nextElement && !nextElement.classList.contains('subHead-1')) {
            if (nextElement.classList.contains('subHead-2')) {
                const li2 = document.createElement('li');
                li2.classList.add('toc-itemo', 'tocSick');
                const tocToggler2 = document.createElement('span');
                tocToggler2.textContent = '[x]';
                tocToggler2.classList.add('tocToggler');
                li2.appendChild(tocToggler2);
                const a2 = document.createElement('a');
                a2.href = '#' + nextElement.id;
                a2.textContent = nextElement.textContent;
                li2.appendChild(a2);
                const subHeads3listo = document.createElement('ul');
                subHeads3listo.classList.add('toc-listo');
                let nextSubElement = nextElement.nextElementSibling;
                
                while (nextSubElement && !nextSubElement.classList.contains('subHead-1') && !nextSubElement.classList.contains('subHead-2')) {
                    if (nextSubElement.classList.contains('subHead-3')) {
                        const li3 = document.createElement('li');
                        li3.classList.add('toc-itemo');
                        const tocToggler3 = document.createElement('span');
                        tocToggler3.textContent = '[]';
                        tocToggler3.classList.add('tocToggler');
                        li3.appendChild(tocToggler3);
                        const a3 = document.createElement('a');
                        a3.href = '#' + nextSubElement.id;
                        a3.textContent = nextSubElement.textContent;
                        li3.appendChild(a3);
                        subHeads3listo.appendChild(li3);
                    }
                    nextSubElement = nextSubElement.nextElementSibling;
                }
                
                if (subHeads3listo.children.length > 0) {
                    li2.appendChild(subHeads3listo);
                } else {
                    tocToggler2.textContent = '[]';
                }
                
                subHeads2listo.appendChild(li2);
            }
            nextElement = nextElement.nextElementSibling;
        }
        
        if (subHeads2listo.children.length > 0) {
            li1.appendChild(subHeads2listo);
        } else {
            tocToggler.textContent = '[]';
        }
        toc.appendChild(li1);
    });

    document.querySelectorAll('.tocToggler').forEach(function(icon) {
        icon.addEventListener('click', function(event) {
            event.stopPropagation();
            const tocItem = this.parentNode;
            const subList = tocItem.querySelector('.toc-listo');
            
            if (subList) {
                if (subList.style.display === 'block') {
                    subList.style.display = 'none';
                    this.textContent = '[]';
                } else {
                    subList.style.display = 'block';
                    this.textContent = '[x]';
                }
            } else {
                this.textContent = this.textContent === '[]' ? '[x]' : '[]';
            }
        });
    });
});
