document.addEventListener('DOMContentLoaded', function() {
    const calendarEl = document.getElementById('calendar');
    const currentDate = new Date();
    const currentMonth = currentDate.getMonth();
    const currentYear = currentDate.getFullYear();
    let selectedDay = null;

    function renderCalendar(month, year) {
        calendarEl.innerHTML = '';
        const daysInMonth = new Date(year, month + 1, 0).getDate();
        const firstDay = new Date(year, month, 1).getDay();

        // Render header
        const daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        daysOfWeek.forEach(day => {
            const headerEl = document.createElement('div');
            headerEl.classList.add('header');
            headerEl.textContent = day;
            calendarEl.appendChild(headerEl);
        });

        // Render empty cells for days before the first day of the month
        for (let i = 0; i < firstDay; i++) {
            const emptyCell = document.createElement('div');
            calendarEl.appendChild(emptyCell);
        }

        // Render days of the month
        for (let day = 1; day <= daysInMonth; day++) {
            const dayCell = document.createElement('div');
            dayCell.textContent = day;
            dayCell.dataset.date = new Date(year, month, day).toISOString();dayCell.addEventListener('click', () => {
                selectedDay = new Date(year, month, day);
                displayDayDetails(selectedDay);
        });
            calendarEl.appendChild(dayCell);
        }
    }

    function loadEvents() {
        fetch('/calendar/event_data/')
            .then(response => response.json())
            .then(events => {
                events.forEach(event => {
                    const eventDate = new Date(event.start);
                    if (eventDate.getMonth() === currentMonth && eventDate.getFullYear() === currentYear) {
                        const dayCell = calendarEl.children[eventDate.getDate() + 6]; // Adjust for header and empty cells
                        const eventEl = document.createElement('div');
                        eventEl.textContent = event.title;
                        eventEl.style.backgroundColor = '#ffcc00';
                        dayCell.appendChild(eventEl);
                    }
                });
            });
    }

    function displayDayDetails(date) {
        const dayDetailsEl = document.getElementById('day-details');
        dayDetailsEl.innerHTML = '<h2>Events on ${date.toDateString()}</h2>';
        fetch('/calendar/event_data/')
            .then(response => response.json())
            .then(events => {
                const dayEvents = events.filter(event => {
                    const eventDate = new Date(event.start);
                    return eventDate.toDateString() === date.toDateString();
                });
                dayEvents.forEach(event => {
                    const eventEl = document.createElement('div');
                    eventEl.textContent = event.title;
                    dayDetailsEl.appendChild(eventEl);
                });
            });
    }

    renderCalendar(currentMonth, currentYear);
    loadEvents();
});