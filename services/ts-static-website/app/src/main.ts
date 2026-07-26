const app = document.getElementById('app');

if (app) {
  const header = document.createElement('header');
  header.innerHTML = `
    <h1>TS Static Website</h1>
    <p>TypeScript と Vite で構築したモダンな静的サイトです。</p>
  `;

  const main = document.createElement('main');
  main.innerHTML = `
    <section>
      <p>このページは TypeScript から DOM を生成しています。</p>
      <p>Vite を使うことでモダンな開発体験が可能です。</p>
    </section>
  `;

  const footer = document.createElement('footer');
  footer.innerHTML = `
    <p>&copy; 2026 ts-static-website</p>
  `;

  app.append(header, main, footer);
} else {
  console.error('App root element not found');
}
