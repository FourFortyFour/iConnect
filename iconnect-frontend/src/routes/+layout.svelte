<script>
  import Nav from "../components/Nav.svelte";
  import Footer from "../components/Footer.svelte";
  // export const prerender = true;
</script>

<svelte:head>
  <link rel="icon" type="image/x-icon" href="/logos/logo-black.ico">
</svelte:head>

<Nav />
<slot />
<Footer />

<style>
  @import url("https://fonts.googleapis.com/css2?family=Cabin+Condensed&display=swap");

  * {
    height: 100vh;
    margin: 0;
    font-family: "Cabin Condensed", sans-serif;
  }
  :root {
    position: relative;
    min-height: 100vh;
  }
</style>
