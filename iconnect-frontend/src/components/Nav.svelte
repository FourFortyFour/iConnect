<script>
  import { fade } from "svelte/transition";
  import { onMount } from "svelte";
  let open = false;

  let handlePhoneMenuClick = (event) => {
    !event.target.closest(".active-dropdown") &&
    !event.target.closest(".phone-dropdown")
      ? (open = false)
      : null;
  };

  onMount(() => {
    document.body.addEventListener("click", handlePhoneMenuClick);
    return () => {
      document.body.removeEventListener("click", handlePhoneMenuClick);
    };
  });
</script>

<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,700,1,0"
/>
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
</header>
{#if !open}
  <button class="phone-dropdown" on:click={() => (open = !open)}>
    <div />
    <div />
    <div />
  </button>
{/if}

{#if open}
  <div class="active-dropdown" in:fade={{ delay: 300 }}>
    <a href="/">
      <img
        class="dropdown-logo"
        src="/logos/logo-no-background.png"
        draggable="false"
        alt="logo"
      />
    </a>
    <a class="dropdown-item" href="/contact">CONTACT</a>
    <a class="dropdown-item" href="/order">GET YOUR OWN</a>
  </div>
{/if}

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");
  * {
    box-sizing: border-box;
    margin: 0;
    font-family: "Cabin Condensed", sans-serif;
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
    position: fixed;
    align-items: center;
    justify-content: space-around;
    width: 3rem;
    height: 3rem;
    background: #444444be;
    border-radius: 50%;
    top: 1em;
    cursor: pointer;
    left: calc(50% - 1.5rem);
    z-index: 10;
  }

  .phone-dropdown > div {
    width: 1.5rem;
    height: 0.25rem;
    background: #000000;
    border-radius: 10px;
    transition: all 0.3s linear;
    /* position: relative; */
    transform-origin: 1px;
  }
  .active-dropdown {
    position: fixed;
    background-color: #444444;
    width: 100%;
    display: flex;
    flex-direction: column;
    padding: 10px;
    align-items: center;
    justify-content: center;
    z-index: 10;
  }
  .active-dropdown .dropdown-logo {
    width: 50px;
    margin-bottom: 10px;
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
    .nav_links,
    .navbar {
      display: none;
    }

    .logo {
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
