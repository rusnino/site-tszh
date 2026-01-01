const Home = () => {
  return (
    <div className="grid">
      <section className="card">
        <h1>Цифровой сервис для вашего дома</h1>
        <p>
          Подавайте заявки, отслеживайте статусы, общайтесь с диспетчером и
          получайте отчеты по работам прямо в личном кабинете.
        </p>
      </section>
      <section className="grid grid-3">
        <div className="card">
          <h3>Прозрачная обработка</h3>
          <p>Все действия фиксируются, заявка проходит все этапы работы.</p>
        </div>
        <div className="card">
          <h3>Мобильный доступ</h3>
          <p>Личный кабинет доступен с любого устройства.</p>
        </div>
        <div className="card">
          <h3>Служба поддержки</h3>
          <p>Диспетчер и мастер всегда в контакте с жильцом.</p>
        </div>
      </section>
    </div>
  );
};

export default Home;
