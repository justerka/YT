const image = document.getElementById('cover'),
    title = document.getElementById('music-title'),
    artist = document.getElementById('music-artist'),
    currentTimeEl = document.getElementById('current-time'),
    durationEl = document.getElementById('duration'),
    progress = document.getElementById('progress'),
    playerProgress = document.getElementById('player-progress'),
    prevBtn = document.getElementById('prev'),
    nextBtn = document.getElementById('next'),
    playBtn = document.getElementById('play'),
    background = document.getElementById('bg-img');

const music = new Audio();
// музыкалар
const songs = [
    {
        path: 'Music/91.mp3',
        displayName: 'Қалай қарайсың',
        cover: 'Photo/91.jpg',
        artist: 'Ninety one',
    },
    {
        path: 'Music/adele.mp3',
        displayName: 'Rolling in the deep',
        cover: 'Photo/adele.jpg',
        artist: 'Adele',
    },
    {
        path: 'Music/Amy.mp3',
        displayName: 'Demon slayer',
        cover: 'Photo/amy.jpg',
        artist: 'Amy B',
    },
    {
        path: 'Music/5000.mp3',
        displayName: '5000',
        cover: 'Photo/5000.jpg',
        artist: 'Ирина Кайратовна',
    },
    {
        path: 'Music/mooz.mp3',
        displayName: 'mooz',
        cover: 'Photo/mooz.jpg',
        artist: 'Ninety one',
    },
    {
        path: 'Music/erikpe.mp3',
        displayName: 'Erikpe',
        cover: 'Photo/tbrn.jpg',
        artist: 'Darkhan juzz',
    },
    {
        path: 'Music/Tunde.mp3',
        displayName: 'Tunde',
        cover: 'Photo/arshat.jpeg',
        artist: 'Arshat',
    },
    {
        path: 'Music/ac_dc.mp3',
        displayName: 'Back in black',
        cover: 'Photo/ac.jpeg',
        artist: 'AC/DC',
    },
    {
        path: 'Music/september.mp3',
        displayName: 'September',
        cover: 'Photo/september.jpeg',
        artist: 'Earth',
    },
    {
        path: 'Music/jyn.mp3',
        displayName: 'JЫN ҰRADЫ',
        cover: 'Photo/jyn.jpeg',
        artist: 'NAZZARBECK',
    },
    {
        path: 'Music/ai.mp3',
        displayName: 'Айыптама',
        cover: 'Photo/91.jpg',
        artist: 'Ninety one',
    },
    {
        path: 'Music/sara.mp3',
        displayName: 'Мен сені сағындым',
        cover: 'Photo/sara.jpeg',
        artist: 'Сара Амангелді',
    },
    {
        path: 'Music/tgg.mp3',
        displayName: 'T.G.G',
        cover: 'Photo/tgg.jpeg',
        artist: 'Santiz',
    },
    {
        path: 'Music/santiz.mp3',
        displayName: 'Забытый бала',
        cover: 'Photo/tgg.jpeg',
        artist: 'Santiz',
    },
];

let musicIndex = 0;
let isPlaying = false;

function togglePlay() {
    if (isPlaying) {
        pauseMusic();
    } else {
        playMusic();
    }
}

function playMusic() {
    isPlaying = true;
    // плей иконка
    playBtn.classList.replace('fa-play', 'fa-pause');
    // титл
    playBtn.setAttribute('title', 'Pause');
    music.play();
}

function pauseMusic() {
    isPlaying = false;
    // пауза иконка
    playBtn.classList.replace('fa-pause', 'fa-play');
    // титл
    playBtn.setAttribute('title', 'Play');
    music.pause();
}

function loadMusic(song) {
    music.src = song.path;
    title.textContent = song.displayName;
    artist.textContent = song.artist;
    image.src = song.cover;
    background.src = song.cover;
}

function changeMusic(direction) {
    musicIndex = (musicIndex + direction + songs.length) % songs.length;
    loadMusic(songs[musicIndex]);
    playMusic();
}

function updateProgressBar() {
    const { duration, currentTime } = music;
    const progressPercent = (currentTime / duration) * 100;
    progress.style.width = `${progressPercent}%`;

    const formatTime = (time) => String(Math.floor(time)).padStart(2, '0');
    durationEl.textContent = `${formatTime(duration / 60)}:${formatTime(duration % 60)}`;
    currentTimeEl.textContent = `${formatTime(currentTime / 60)}:${formatTime(currentTime % 60)}`;
}

function setProgressBar(e) {
    const width = playerProgress.clientWidth;
    const clickX = e.offsetX;
    music.currentTime = (clickX / width) * music.duration;
}

playBtn.addEventListener('click', togglePlay);
prevBtn.addEventListener('click', () => changeMusic(-1));
nextBtn.addEventListener('click', () => changeMusic(1));
music.addEventListener('ended', () => changeMusic(1));
music.addEventListener('timeupdate', updateProgressBar);
playerProgress.addEventListener('click', setProgressBar);

loadMusic(songs[musicIndex]);
