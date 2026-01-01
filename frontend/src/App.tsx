import { Link, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Contacts from "./pages/Contacts";
import Login from "./pages/Login";
import Register from "./pages/Register";
import ResidentDashboard from "./pages/ResidentDashboard";
import CreateTicket from "./pages/CreateTicket";
import TicketList from "./pages/TicketList";
import TicketDetails from "./pages/TicketDetails";
import AdminDashboard from "./pages/AdminDashboard";
import AdminTicketInbox from "./pages/AdminTicketInbox";
import AdminTicketDetails from "./pages/AdminTicketDetails";
import AdminUsers from "./pages/AdminUsers";
import AdminAuditLog from "./pages/AdminAuditLog";

const App = () => {
  return (
    <div className="app-shell">
      <header className="app-header">
        <div className="brand">ТСЖ Онлайн</div>
        <nav>
          <Link to="/">Главная</Link>
          <Link to="/contacts">Контакты</Link>
          <Link to="/resident">Кабинет</Link>
          <Link to="/admin">Админка</Link>
        </nav>
        <div className="auth-links">
          <Link to="/login">Вход</Link>
          <Link to="/register">Регистрация</Link>
        </div>
      </header>
      <main className="app-main">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/contacts" element={<Contacts />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          <Route path="/resident" element={<ResidentDashboard />} />
          <Route path="/resident/tickets/new" element={<CreateTicket />} />
          <Route path="/resident/tickets" element={<TicketList />} />
          <Route path="/resident/tickets/:id" element={<TicketDetails />} />

          <Route path="/admin" element={<AdminDashboard />} />
          <Route path="/admin/tickets" element={<AdminTicketInbox />} />
          <Route path="/admin/tickets/:id" element={<AdminTicketDetails />} />
          <Route path="/admin/users" element={<AdminUsers />} />
          <Route path="/admin/audit" element={<AdminAuditLog />} />
        </Routes>
      </main>
    </div>
  );
};

export default App;
