<script>
  import Nav from "../components/Nav.svelte";
  import Footer from "../components/Footer.svelte";
</script>

<Nav />
<slot />
<Footer />

<style>
  * {
    height: 100vh;
    margin: 0;
  }
  :root {
    position: relative;
    min-height: 100vh;
  }
</style>
