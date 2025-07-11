--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11
-- Dumped by pg_dump version 14.11

-- Started on 2025-06-16 15:03:25

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4228 (class 1262 OID 85654)
-- Name: chipaque; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE chipaque WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'es_CO.UTF-8' LC_CTYPE = 'es_CO.UTF-8';


ALTER DATABASE chipaque OWNER TO postgres;

\connect chipaque

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 86738)
-- Name: predio; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.predio (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    localizacion point,
    estado integer,
    celular character varying(13),
    direccion character varying(150)
);


ALTER TABLE public.predio OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 86737)
-- Name: predio_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.predio_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.predio_id_seq OWNER TO postgres;

--
-- TOC entry 4229 (class 0 OID 0)
-- Dependencies: 215
-- Name: predio_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.predio_id_seq OWNED BY public.predio.id;


--
-- TOC entry 4074 (class 2604 OID 86741)
-- Name: predio id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.predio ALTER COLUMN id SET DEFAULT nextval('public.predio_id_seq'::regclass);


--
-- TOC entry 4222 (class 0 OID 86738)
-- Dependencies: 216
-- Data for Name: predio; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 4230 (class 0 OID 0)
-- Dependencies: 215
-- Name: predio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.predio_id_seq', 1, false);


--
-- TOC entry 4076 (class 2606 OID 86743)
-- Name: predio predio_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.predio
    ADD CONSTRAINT predio_pkey PRIMARY KEY (id);


-- Completed on 2025-06-16 15:03:25

--
-- PostgreSQL database dump complete
--

