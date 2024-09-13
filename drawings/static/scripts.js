// Function to toggle theme and save to localStorage
function toggleTheme() {
    const themeSwitch = document.getElementById('theme-toggle-checkbox');
    const currentTheme = themeSwitch.checked;

    if (currentTheme) {
        document.body.classList.add('dark-theme');
        localStorage.setItem('theme', 'dark');
        document.getElementById('theme-label').textContent = 'Dark Mode';
    } else {
        document.body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light');
        document.getElementById('theme-label').textContent = 'Light Mode';
    }
}

// Function to load the theme based on localStorage
function loadTheme() {
    const storedTheme = localStorage.getItem('theme');
    const themeSwitch = document.getElementById('theme-toggle-checkbox');

    if (storedTheme === 'dark') {
        document.body.classList.add('dark-theme');
        themeSwitch.checked = true;
        document.getElementById('theme-label').textContent = 'Dark Mode';
    } else {
        document.body.classList.remove('dark-theme');
        themeSwitch.checked = false;
        document.getElementById('theme-label').textContent = 'Light Mode';
    }
}

// Ensure that this script runs on page load
document.addEventListener('DOMContentLoaded', function() {
    loadTheme();
    const themeSwitch = document.getElementById('theme-toggle-checkbox');
    if (themeSwitch) {
        themeSwitch.addEventListener('change', toggleTheme);
    }
});
