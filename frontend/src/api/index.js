import { httpClient } from "../plugins/httpClient";

export default {
  login(email, password) {
    return httpClient.post("/api/login/", { email, password });
  },
  logout() {
    return httpClient.get("/api/logout/");
  },
  authCheck() {
    return httpClient.get("/api/auth-check/");
  }
};
