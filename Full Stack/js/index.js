

const posts = [
    {
        title: 'Why you should learn Javascript',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec dictum mollis leo, et ultrices justo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam et lacus in mauris mattis auctor vel quis lectus. Nunc tellus nunc, fermentum sed ipsum nec, commodo pharetra odio. Curabitur molestie vestibulum nibh ac vulputate. Sed est libero, ultrices sed eleifend eget, tempus accumsan ipsum. Sed viverra nec mauris eget rhoncus. Suspendisse eu sapien id lorem sodales feugiat. Donec lectus arcu, tempor dignissim feugiat accumsan, tempor sit amet velit. Maecenas nulla urna, consectetur id lectus euismod, varius tincidunt justo. Nulla pulvinar vehicula tincidunt. Suspendisse pharetra, massa ut pharetra porttitor, lacus mauris consectetur purus, ut faucibus lacus nulla eu elit. Donec et tellus sodales, ultrices ex et, vulputate turpis. Pellentesque pretium neque sit amet lorem cursus tristique. Mauris et sollicitudin velit. Morbi ornare, sapien euismod malesuada vestibulum, ante lorem condimentum enim, eget ornare odio ex sed dui.',
        image: './Images/javascript_img1.jpeg' 
    },

    {
        title: 'Why react is a cool library',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec dictum mollis leo, et ultrices justo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam et lacus in mauris mattis auctor vel quis lectus. Nunc tellus nunc, fermentum sed ipsum nec, commodo pharetra odio. Curabitur molestie vestibulum nibh ac vulputate. Sed est libero, ultrices sed eleifend eget, tempus accumsan ipsum. Sed viverra nec mauris eget rhoncus. Suspendisse eu sapien id lorem sodales feugiat. Donec lectus arcu, tempor dignissim feugiat accumsan, tempor sit amet velit. Maecenas nulla urna, consectetur id lectus euismod, varius tincidunt justo. Nulla pulvinar vehicula tincidunt. Suspendisse pharetra, massa ut pharetra porttitor, lacus mauris consectetur purus, ut faucibus lacus nulla eu elit. Donec et tellus sodales, ultrices ex et, vulputate turpis. Pellentesque pretium neque sit amet lorem cursus tristique. Mauris et sollicitudin velit. Morbi ornare, sapien euismod malesuada vestibulum, ante lorem condimentum enim, eget ornare odio ex sed dui.',
        image: './Images/react_img.png'
    },

    {
        title: 'Software Engineering pays well',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec dictum mollis leo, et ultrices justo. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam et lacus in mauris mattis auctor vel quis lectus. Nunc tellus nunc, fermentum sed ipsum nec, commodo pharetra odio. Curabitur molestie vestibulum nibh ac vulputate. Sed est libero, ultrices sed eleifend eget, tempus accumsan ipsum. Sed viverra nec mauris eget rhoncus. Suspendisse eu sapien id lorem sodales feugiat. Donec lectus arcu, tempor dignissim feugiat accumsan, tempor sit amet velit. Maecenas nulla urna, consectetur id lectus euismod, varius tincidunt justo. Nulla pulvinar vehicula tincidunt. Suspendisse pharetra, massa ut pharetra porttitor, lacus mauris consectetur purus, ut faucibus lacus nulla eu elit. Donec et tellus sodales, ultrices ex et, vulputate turpis. Pellentesque pretium neque sit amet lorem cursus tristique. Mauris et sollicitudin velit. Morbi ornare, sapien euismod malesuada vestibulum, ante lorem condimentum enim, eget ornare odio ex sed dui.',
        image: './Images/software_img.jpeg'
    }

];



// can also define function as 
// const createPost = (post) =>{
// define funtion here
//}
// Use a function to dynamically generate HTML

function createPost(post) {
    const postSrings =  `
    <div class="preview">
                <div>
                    <!-- Title of content-->
                    <h2>${post.title}</h2>
                    <p class="preview-text">
                        ${post.description}
                    </p>
                    <a href="./post/javascript.html">Read more ...</a>
                </div>
                <div>
                    <!-- Image-->
                    <img
                    class="preview-image"
                    src="${post.image}" 
                    />
                </div>

                

            </div>
    `;
    previews.innerHTML += postSrings 
}

// Interration loop 
posts.forEach(createPost);





