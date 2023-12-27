
// ########## SOCKET IO ########## //
let isConnected = false
let socket = io(document.location.pathname, {autoConnect: false});
// let socket = io();
socket.on('connect', function() {
    isConnected = true
    socket.emit('connected', {rcode: $('.cell-code').text()});
});
socket.on('disconnect', function() {
    isConnected = false
    // socket.emit('connected', {rcode: $('.cell-code').text()});
});

const msgInput = $('#msgSender input');
msgInput.on('keydown', e => {
    if (e.key === 'Enter') {
        if (msgInput.val() === 'connect') {
            socket.connect();
            msgInput.val('');
            return
        }
        sendMsg();
    };
})
const terminal = document.getElementById('msg-terminal')
const msgSender = document.getElementById('msgSender')
function sendMsg() {
    const msg = msgInput.val().trim();
    if(isConnected && msg || true){
        socket.emit('message', {msg: msg});
        const message = document.createElement('div');
        message.className = 'msg';
        message.innerHTML =`<div class="msg">
                                <span class="user-nick">&lt; testy&gt;:</span>
                                <p>${msg}</p>
                            </div>`;
        terminal.appendChild(message);
        terminal.insertBefore(message, msgSender);
        console.log(msgSender);
    }
    msgInput.val('');
};

socket.on('message', (data) => {
    // $('.cell-code').html(data.msg);
    console.log(data.msg);
});

function joinCell(cell) {
    
}



// ########### COOL SIDE PANELS ########### //
const asidePanels = document.querySelectorAll('.side-panels')
asidePanels.forEach(asidePanel => {

    const sidePanels = asidePanel.querySelectorAll('.side-panel')
    sidePanels.forEach(sidePanel => {

        const panelTitle = sidePanel.querySelector('span.side-panel-title');
        panelTitle.addEventListener('click', e => {
            // const preActivePanel = mainPanel.querySelector('section.spanel-focus');
            // console.log(mainPanel, preActivePanel);
            e.preventDefault();
            sidePanel.classList.toggle('spanel-focus');
            sidePanel.classList.toggle('cursor-pointer');
            sidePanel.classList.toggle('spanel-hover');
        }); // remove hover effect and cursor pointer when clicked title of panel and open it. click again to vice versa
        // panelTitle.addEventListener('blur', () => {
        //     console.log("blurred")
        //     sidePanel.classList.toggle('cursor-pointer');
        //     sidePanel.classList.toggle('spanel-focus');
        //     sidePanel.classList.toggle('spanel-hover');
        // });
    });
}); // add futuristic hecker hover and open effect on panels in both side panels

// ********* TABS ********* //
document.querySelectorAll('.side-panel-categories, .category-subcategories').forEach(ele => {
    ele.addEventListener('click', (e) => {
        changeTab(e);
        // console.log('event:\n', e, '\n\n', e.target.closest('span'));
    });
}); // add click event listener to all category nav bars in side-panels 

const tabContentClasses = {
    'category': 'category-content', 
    'subcategory': 'subcategory-content', 
}; // category content class corresponding to nav category class

function changeTab(event) {
    const clickedTab = event.target.closest('span');
    if (!clickedTab) return;
    if (clickedTab.classList.contains('active-category')) return;

    const clickedTabClass = clickedTab.className;
    const contentClass = tabContentClasses[clickedTabClass];
    const contentToActive = clickedTab.getAttribute('data-for-tab');
    const superParent = clickedTab.parentNode.parentNode;
    const clickedTabContent = superParent.querySelector(`.${contentClass}[data-tab="${contentToActive}"]`);

    // console.log('To activate Tab class: ', clickedTabClass);
    // console.log('corresponding section(content) class: ', contentClass);

    // console.log('Tab To deactivate: ');
        clickedTab.parentNode.querySelector('.active-category').classList.remove('active-category')
    // console.log('Tab To activate: ');
        clickedTab.classList.add('active-category')

    // console.log('content To deactivate: ');
        superParent.querySelector(`.${contentClass}.${contentClass}-active`).classList.remove(`${contentClass}-active`)
    // console.log('content To activate: ');
        clickedTabContent.classList.add(`${contentClass}-active`)

    if (clickedTabContent.querySelector('nav')) { // clickedTabClass === 'category'
        const firstSubTab = clickedTabContent
            .querySelector(`.subcategory-content.subcategory-content-active`);

        // console.log(firstSubTab || 'No active Sub Tab');

        if (!firstSubTab) {
            // console.log();
            clickedTabContent.querySelector('nav .subcategory[data-for-tab]').classList.add('active-category');
            // console.log();
            clickedTabContent.querySelector(`.subcategory-content[data-tab]`).classList.add('subcategory-content-active');
        };
    };
};



// ########### Actions PANEL ########### //
const createCellMenu = document.getElementById('create-cell-menu');
function createCell(e) {
    e.preventDefault()
    if (createCellMenu.classList.contains('hidden')) {toggleCreateCellMenu(); return;};

    let url = $(this).closest('form').attr('action'),
        data = $(this).closest('form').serialize();
    $.ajax({
        url: url,
        type: 'post',
        data: data,
        success: function(){
           // Whatever you want to do after the form is successfully submitted
        }
   });
    
    // const msgTerminal = document.getElementById('msg-terminal');
    // let calHeight;
    // if (createCellMenu.classList.contains('hidden')) {
    //     calHeight = `${parseFloat(getComputedStyle(msgTerminal).height.replace('px', '')) - parseFloat(getComputedStyle(createCellMenu).height.replace('px', ''))}px`;
    // } else {
    //     calHeight = `${parseFloat(getComputedStyle(msgTerminal).height.replace('px', '')) + parseFloat(getComputedStyle(createCellMenu).height.replace('px', ''))}px`;
    // };
    // console.log(calHeight);
    
    // msgTerminal.style.setProperty('height', calHeight);
}

function toggleCreateCellMenu(e=null) {
    if (e) {e.preventDefault();};
    if (createCellMenu.classList.contains('hidden')) {
        createCellMenu.classList.remove('hidden');
        document.getElementById('createCellMenuToggler').textContent = '▼'
    } else {
        createCellMenu.classList.add('hidden');
        document.getElementById('createCellMenuToggler').textContent = '▲'
    };
}



