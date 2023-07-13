<nav>
    
    <ul>
        <li><a href="/">Home</a></li>
        <li>Our Product</li>
        <li>Contact</li>
        <li>About Us</li>
    </ul>
</nav>

<slot />

<style>
    * {
        box-sizing: border-box;
        margin: 0;
    }
    ul {
        display: flex;
    }
    li{
        list-style: none;
        padding: 0 1%;
        color: white
    }
    a {
        color: white;
    }
    nav {
        background-color: black;
        padding: 2% 0;
    }
</style>