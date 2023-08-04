<script>
  import SpinningCard from "../components/SpinningCard.svelte";
  import Wave from "../components/LandingPageAssests/Wave.svelte";
  import BuyLink from "../components/LandingPageAssests/BuyLink.svelte";
  import HeroText from "../components/LandingPageAssests/HeroText.svelte";
  import Spacer from "../components/LandingPageAssests/Spacer.svelte";
  import About from "../components/About.svelte";
</script>


<Spacer />
<section class="home">
  <HeroText />
  <BuyLink/>
  <SpinningCard></SpinningCard>
  <Wave />
</section>
<About />

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

  * {
    font-family: "Cabin Condensed", sans-serif;
  }
  @keyframes bepur {
    0% {
      fill: #6ee2f5;
    }
    100% {
      fill: #8c1cff;
    }
  }

  @keyframes beblue {
    0% {
      fill: #8c1cff;
    }
    100% {
      fill: #6ee2f5;
    }
  }

  @keyframes opac {
    0% {
      fill-opacity: 0%;
    }
    100% {
      fill-opacity: 80%;
    }
  }

  .home {
    position: relative;

    display: grid;
    grid-template-columns: 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw 2vw;
    grid-template-rows: 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh 2vh;
    align-items: center;

    height: 100vh;
    width: 100vw;
  }

  /* Landing links */

  

  /* End of links */
  
</style>
