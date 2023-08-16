<script>
  import { fly } from "svelte/transition";
  import { onMount } from "svelte";

  let open = false;

  let closeDropdown = () => {
    open = false;
  };
  onMount(() => {
    window.addEventListener("click", closeDropdown);
    return () => {
      window.removeEventListener("click", closeDropdown);
    };
  });
</script>

<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,700,1,0"
/>
<!-- <meta name="viewport" content="width=device-width, initial-scale=1.0" /> -->
<header class="navbar" id="navbar">
  <a href="/" class="icon-link">
    <img
      class="logo"
      src="/logos/logo-no-background.png"
      draggable="false"
      alt="logo"
    />
  </a>
  <nav>
    <ul class="nav_links">
      <li class="navitem"><a href="/contact">CONTACT</a></li>
      <li class="navitem"><a href="/order">GET YOUR OWN</a></li>
    </ul>
  </nav>
  <dt />
  <button
    class="phone-dropdown"
    on:click={(event) => {
      open = !open;
      event.stopPropagation();
    }}
  >
    <div />
    <div />
    <div />
  </button>
  {#if open}
    <div
      class="active-dropdown"
      transition:fly|global={{ y: -100, duration: 1000 }}
      on:click={(event) => event.stopPropagation()}
    >
      <a class="dropdown-item" href="/contact">CONTACT</a>
      <a class="dropdown-item" href="/order">GET YOUR OWN</a>
    </div>
  {/if}
</header>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");
  * {
    box-sizing: border-box;
    margin: 0;
    font-family: "Cabin Condensed", sans-serif;
    z-index: 2;
  }

  .navbar {
    position: sticky;
    top: 2vh;
    /* top: 2rem; */
    margin: 2vh 0.5vw 0;
    /* grid-area: 2/2/2/12; */
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;

    background-color: #444444be;
    backdrop-filter: blur(20px);
    border-radius: 50px;

    transition: all 500ms ease-in-out 0s;
    user-select: none;
    z-index: 4;
    padding: 3vh 0;
    /* padding: 1rem 2rem; */
  }

  .navbar:hover {
    background-color: #444444;
  }

  .navbar:n .nav_links {
    list-style: none;
  }

  .nav_links li {
    display: inline-block;
    /* padding: 0px 50px; */
    padding: 0 1rem;
  }

  .nav_links li a {
    transition: all 500ms ease-in-out 0s;
    font-size: 1.7rem;
  }

  .nav_links li a:hover {
    font-size: 2rem;
    font-weight: 700;
    color: #6ee2f5;
    letter-spacing: 10px;
  }

  .navitem,
  .navitem a {
    font-family: "Cabin Condensed";
    font-weight: 600px;
    font-size: 25px;
    color: #ffffff;
    text-decoration: none;
    letter-spacing: 7px;
  }

  .navitem a:hover {
    letter-spacing: 12px;
  }

  .logo {
    padding-left: 20px;
    width: 100%;
    cursor: pointer;
    user-select: none;
  }

  .icon-link {
    width: 5%;
  }
  .phone-dropdown {
    display: none;
    flex-direction: column;
    justify-content: space-around;
    width: 2rem;
    height: 2rem;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    z-index: 10;
  }

  .phone-dropdown > div {
    width: 100%;
    height: 0.25rem;
    background: #ffffff;
    border-radius: 10px;
    transition: all 0.3s linear;
    /* position: relative; */
    transform-origin: 1px;
  }
  .active-dropdown {
    position: absolute;
    top: 100%;
    left: 0;
    background-color: #444444;
    width: 100vw;
    display: flex;
    flex-direction: column;
    padding: 10px;
    align-items: center;
  }

  .active-dropdown .dropdown-item {
    color: #ffffff;
    padding: 10px;
    text-decoration: none;
    font-family: "Cabin Condensed";
    font-weight: 600;
    font-size: 20px;
    letter-spacing: 7px;
  }

  .active-dropdown .dropdown-item:hover {
    color: #6ee2f5;
  }
  @media (max-width: 768px) {
    nav {
      display: none;
    }
    .navbar {
      position: sticky;
      border-radius: 0%;
      top: 0;
      margin: 0;
      padding: 3.5%;
      background-color: #444444;
      width: 100vw;
      /* height: 7vh; */
    }

    .logo {
      padding-left: 0%;
    }

    .icon-link {
      width: 12vw;
    }
    .nav_links {
      display: none;
    }

    .phone-dropdown {
      display: flex;
    }

    .nav_links li a {
      font-size: 1rem;
    }
  }
  /* .clearing {
    margin-bottom: 7%;
    opacity: 0%;
  } */
</style>
