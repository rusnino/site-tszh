import { Link } from "react-router-dom";

const ResidentDashboard = () => {
  return (
    <div className="grid">
      <section className="card">
        <h1>Личный кабинет</h1>
        <p>Здесь отображаются ваши заявки и уведомления от управляющей компании.</p>
      </section>
      <section className="grid grid-3">
        <div className="card">
          <h3>Создать заявку</h3>
          <p>Опишите проблему и прикрепите фото.</p>
          <Link className="button" to="/resident/tickets/new">
            Новая заявка
          </Link>
        </div>
        <div className="card">
          <h3>Мои заявки</h3>
          <p>Отслеживайте статусы и сроки.</p>
          <Link className="button" to="/resident/tickets">
            Перейти
          </Link>
        </div>
        <div className="card">
          <h3>Новости дома</h3>
          <p>Плановые работы и уведомления.</p>
          <span className="badge">Обновлено сегодня</span>
        </div>
      </section>
    </div>
  );
};

export default ResidentDashboard;
