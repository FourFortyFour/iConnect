<script>
    import { fade } from "svelte/transition";
    // import { watchResize} from "svelte-watch-resize";
    export let urls;
  
    const size = 4;
    $: prev = 0;
    $: next = 4;
    $: current = urls.slice(prev, next);
  
    $: main_ix = 0;
  
    // $: icon_1 = window.innerWidth <= 425 ? "left" : "up";
    // $: icon_2 = window.innerWidth <= 425 ? "right" : "down";
  
    const bp = 768
  
    $: icon_1 = "up"
    $: icon_2 = "down";
  
    function change_icon() {
        icon_1 = window.innerWidth <= bp ? "left" : "up";
        icon_2 = window.innerWidth <= bp ? "right" : "down"
        console.log(window.innerWidth);
    }
  
    function go_back() {
      if (prev === 0) {
        return -1;
      }
      prev--;
      next--;
    }
  
    function go_next() {
      if (next >= urls.length) {
        console.log(next);
        return -1;
      }
      prev++;
      next++;
    }
  </script>
  
  <!-- <svelte:window on:resize={change_icon}></svelte:window> -->
  
  <link
    rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0"
  />
  
  <div class="caroussel">
    <div class="main-img">
      <img
        class="central-img"
        src={current[main_ix].url}
        out:fade={{ duration: 300 }}
        alt=""
      />
    </div>
    <div class="reel">
      <button on:click={go_back}
        ><span class="material-symbols-outlined"> keyboard_arrow_{icon_1} </span></button
      >
      <section class="reel-items">
        {#each current as url, i}
          {#if main_ix === i}
            <div class="reel-item selected">
              <img
                src={url.url}
                alt={url.alt}
                class="reel-img"
                on:click={() => (main_ix = i)}
              />
            </div>
          {:else}
            <div class="reel-item">
              <img
                src={url.url}
                alt={url.alt}
                class="reel-img"
                on:click={() => (main_ix = i)}
              />
            </div>
          {/if}
        {/each}
        <!-- <div class="reel-item">
            <img src={current[0]} alt="" class="reel-img">
        </div> -->
      </section>
      <button on:click={go_next}>
        <span class="material-symbols-outlined"> keyboard_arrow_{icon_2} </span>
      </button>
    </div>
  </div>
  
  <style>
  
    :root {
      --s : 20vw;
      --primary: #6ee2f5;
    }
    * {
      margin: 0%;
      box-sizing: border-box;
    }
  
    .caroussel {
      display: flex;
      flex-direction: row-reverse;
      align-items: center;
      justify-content: flex-end;
    }
    .outer {
      display: flex;
      height: 100%;
      justify-content: center;
      align-items: center;
    }
    .main-img {
      width: var(--s);
      height: var(--s);
      overflow: hidden;
      border-radius: 25px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .central-img {
      width: 100%;
      transition: opacity 0.3s ease-in-out;
    }
  
    .reel {
      display: flex;
      flex-direction: column;
      margin: 1vh 1vw;
      /* width: 300px; */
      height:  calc(var(--s) * 0.7);
      justify-content: flex-end;
      align-items: center;
    }
  
    .reel-items {
      /* width: 100%; */
      display: flex;
      flex-direction: column;
      height: 100%;
      width: 3.5vw;
    }
  
    .reel-item {
      flex: 0.25;
      border: 1px solid black;
      border-radius: 25%;
      /* margin: 1% 0%; */
      transition: border-color 500ms ease-in-out;
      /* width: 25%; */
      /* width: 5vw; */
      /* height: 5vh; */
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      margin-bottom: 10%;
    }
  
    .selected {
      border: 3px solid var(--primary);
    }
  
    .reel-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  
    .reel-item:hover {
      border-color: var(--primary);
    }
  
    button {
      /* width: 2vw; */
      width: 100%;
      background: none;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
    }
  
    button:hover {
      background-color: rgb(218, 218, 218);
    }
  
    @media (max-width: 768px) {
  
      :root {
        --s: 50vw;
      }
      .caroussel {
        flex-direction: column;
      }
  
      .main-img {
        width: var(--s);
        height: var(--s);
      }
  
      .reel, .reel-items {
        flex-direction: row;
      }
  
      .reel {
        width: 70vw;
        height: auto;
      }
  
      .reel-items {
        width: auto;
        height: auto;
      }
  
      .reel-item {
        margin: 0% 1%;
      }
  
    }
  </style>
  