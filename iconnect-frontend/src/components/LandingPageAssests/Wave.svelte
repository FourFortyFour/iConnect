<div class="wave">
  <svg
    data-name="Layer 1"
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 1200 120"
    preserveAspectRatio="none"
  >
    <path
      d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z"
      class="shape-fill"
      stroke="url(#paint0_linear_3_16)"
      stroke-width="5"
    />
    <!-- <defs>
            <linearGradient id="paint0_linear_3_16" x1="-207.999" y1="-242.501" x2="1456.5" y2="697.5" gradientUnits="userSpaceOnUse">
            <stop stop-color="#8C1CFF"/>
            <stop offset="1" stop-color="#6EE2F5"/>
            </linearGradient>
            </defs> -->
  </svg>
</div>

<style>
  .wave {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100vw;

    /* overflow: hidden; */

    /* line-height: 0; */

    transform: rotate(180deg);

    z-index: 2;
  }

  .wave svg {
    position: relative;
    display: block;
    width: calc(105% + 0.2vw);
    height: 80vh;
  }
  @media (max-width: 768px) {
    .wave svg {
      height: 55vh;
      width: 100vw;
    }
    .wave {
      width: 100vw;
      display: none;
      bottom: 15vh;
      /* z-index: -2; */
    }
  }

  .wave .shape-fill {
    fill: #ffffff;
  }
</style>
