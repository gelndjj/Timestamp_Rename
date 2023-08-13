<a name="readme-top"></a>

[![Contributors][contributors-shield]](https://github.com/gelndjj/Timestamp-Rename/graphs/contributors)
[![Forks][forks-shield]](https://github.com/gelndjj/Timestamp-Rename/forks)
[![Stargazers][stars-shield]](https://github.com/gelndjj/Timestamp-Rename/stargazers)
[![Issues][issues-shield]](https://github.com/gelndjj/Timestamp-Rename/issues)
[![MIT License][license-shield]](https://github.com/gelndjj/Timestamp-Rename/blob/main/LICENSE)
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jonathanduthil/)


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gelndjj/Timestamp_Rename">
    <img src="https://github.com/gelndjj/Timestamp_Rename/blob/main/resources/image.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Timestamp Rename</h3>

  <p align="center">
    A simple way to rename your image/video files by Creation Date !
    <br />
    <a href="https://github.com/gelndjj/Timestamp_Rename"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/gelndjj/Timestamp_Rename/issues">Report Bug</a>
    ·
    <a href="https://github.com/gelndjj/Timestamp_Rename/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
<img src="https://github.com/gelndjj/Timestamp_Rename/blob/main/resources/main_windows.png" alt="Logo" width="700" height="500">
</br>
Flying around is one of my favorite hobby and I often cope with drone's videos renaming on my spare time 'cause my drones have a specific way to rename files that I don't like much.
</br> 
</br>
<img src="https://github.com/gelndjj/Timestamp_Rename/blob/main/resources/drone_video_files.png" alt="Screenshot" width="480" height="320">
</br>
</br>
So, I wrote a small python script that allows me to rename files according to the Creation Date present in the metadata.
Of course, there is a bunch of software that do the same out there and actually I use the built-in function renaming in Lightoom since ages ago but only for pictures. 
</br>
</br>
But, as I sort out my drones videos' files in the finder, I wanted a soft that could do the job for me in no time.This just make every single video file unique.
</br>
</br>
<img src="https://github.com/gelndjj/Timestamp_Rename/blob/main/resources/drone_video_files_sort.png" alt="Screenshot" width="480" height="320">
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

<a href="https://www.python.org">
<img src="https://github.com/gelndjj/Timestamp_Rename/blob/main/resources/py_icon.png" alt="Icon" width="32" height="32">
</a>
&nbsp;
<a href="https://customtkinter.tomschimansky.com">
<img src="https://github.com/gelndjj/Timestamp_Rename/blob/main/resources/ctk_icon.png" alt="Icon" width="32" height="32">
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Rename video files using the timestamp YYYYMMDD_HHMMSS which stand for "Year Month Day _ Hour Minute Second".
</br>
The "Create Folder by Day" checkbox put the files inside folder according to the day. 
</br>
</br>

https://github.com/gelndjj/Timestamp_Rename/assets/81557672/80c9db3d-292e-4a8b-ada2-d4943ff1fd6f

<!-- GETTING STARTED -->
## Standalone APP

Install pyintaller
```
pip install pyinstaller
```
Generate the standalone app
```
pyinstaller --onefile your_script_name.py
```


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU GENERAL PUBLIC LICENSE. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


[LinkedIn](https://github.com/gelndjj/Timestamp-Rename)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
