const videoUrls = [
    "https://www.youtube.com/embed/-QgztwHiH9Y",
    "https://www.youtube.com/embed/80vSF3Hg4F0",
    "https://www.youtube.com/embed/gYsd7AzfY0M",
    "https://www.youtube.com/embed/54DvjhWvLJM",
    "https://www.youtube.com/embed/3EOmBWEaOa4",
    "https://www.youtube.com/embed/K3vI3BWW5Lc",
    "https://www.youtube.com/embed/hXf_HU5_ivc",
    "https://www.youtube.com/embed/YPDDBozimkU"
];

function generateGallery() {
    const galleryContainer = document.querySelectorAll('section')[1].querySelector('.videocontainer');

    // Iterate over the video URLs and create a box for each
    videoUrls.forEach(url => {
        const box = document.createElement('div');
        box.classList.add('box');

        const iframe = document.createElement('iframe');
        iframe.width = 426;
        iframe.height = 240;
        iframe.src = url;

        box.appendChild(iframe);
        galleryContainer.appendChild(box);
    });
}

generateGallery();
